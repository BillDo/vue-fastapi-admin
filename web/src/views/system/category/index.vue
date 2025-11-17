<script setup>
import { h, onMounted, ref, resolveDirective, withDirectives } from 'vue'
import { NButton, NForm, NFormItem, NInput, NInputNumber, NPopconfirm, NSelect, NSwitch, NTag } from 'naive-ui'

import CommonPage from '@/components/page/CommonPage.vue'
import QueryBarItem from '@/components/query-bar/QueryBarItem.vue'
import CrudModal from '@/components/table/CrudModal.vue'
import CrudTable from '@/components/table/CrudTable.vue'
import TheIcon from '@/components/icon/TheIcon.vue'

import { renderIcon } from '@/utils'
import { useCRUD } from '@/composables'
import api from '@/api'

defineOptions({ name: '分类管理' })

const $table = ref(null)
const queryItems = ref({})
const vPermission = resolveDirective('permission')

const {
  modalVisible,
  modalTitle,
  modalLoading,
  handleSave,
  modalForm,
  modalFormRef,
  handleEdit,
  handleDelete,
  handleAdd,
} = useCRUD({
  name: 'Category',
  initForm: { order: 0, is_active: true, image_url: '' },
  doCreate: api.createCategory,
  doUpdate: api.updateCategory,
  doDelete: api.deleteCategory,
  refresh: () => $table.value?.handleSearch(),
})

async function onImageFileChange(e) {
  const file = e?.target?.files?.[0]
  if (!file) return
  try {
    const res = await api.uploadFile(file)
    if (res && res.data && res.data.url) {
      modalForm.image_url = res.data.url
    }
  } catch (err) {
    // ignore; keep existing value
  }
}

onMounted(() => {
  $table.value?.handleSearch()
})

const categoryRules = {
  name: [
    {
      required: true,
      message: '请输入分类名称',
      trigger: ['input', 'blur', 'change'],
    },
  ],
}

const columns = [
  {
    title: '分类名称',
    key: 'name',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '图片',
    key: 'image_url',
    align: 'center',
    width: '140',
    render(row) {
      if (!row.image_url) return '-'
      return h('img', {
        src: row.image_url,
        alt: row.name,
        style: 'width: 80px; height: 60px; object-fit: cover; border-radius: 4px;'
      })
    },
  },
  {
    title: '描述',
    key: 'description',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
  },
  {
    title: '图标',
    key: 'icon',
    align: 'center',
    width: '150',
    ellipsis: { tooltip: true },
  },
  {
    title: '状态',
    key: 'is_active',
    align: 'center',
    width: '100',
    render(row) {
      return h(
        NTag,
        {
          type: row.is_active ? 'success' : 'error',
          size: 'small',
        },
        { default: () => (row.is_active ? '启用' : '禁用') }
      )
    },
  },
  {
    title: '排序',
    key: 'order',
    align: 'center',
    width: '80',
  },
  {
    title: '操作',
    key: 'actions',
    width: 'auto',
    align: 'center',
    fixed: 'right',
    render(row) {
      return [
        withDirectives(
          h(
            NButton,
            {
              size: 'small',
              type: 'primary',
              style: 'margin-left: 8px;',
              onClick: () => handleEdit(row),
            },
            {
              default: () => '编辑',
              icon: renderIcon('material-symbols:edit', { size: 16 }),
            }
          ),
          [[vPermission, 'post/api/v1/category/update']]
        ),
        h(
          NPopconfirm,
          {
            onPositiveClick: () => handleDelete({ id: row.id }, false),
            onNegativeClick: () => {},
          },
          {
            trigger: () =>
              withDirectives(
                h(
                  NButton,
                  {
                    size: 'small',
                    type: 'error',
                    style: 'margin-left: 8px;',
                  },
                  {
                    default: () => '删除',
                    icon: renderIcon('material-symbols:delete-outline', { size: 16 }),
                  }
                ),
                [[vPermission, 'delete/api/v1/category/delete']]
              ),
            default: () => h('div', {}, '确定删除该分类吗?'),
          }
        ),
      ]
    },
  },
]
</script>

<template>
  <!-- 业务页面 -->
  <CommonPage show-footer title="分类列表">
    <template #action>
      <div>
        <NButton
          v-permission="'post/api/v1/category/create'"
          class="float-right mr-15"
          type="primary"
          @click="handleAdd"
        >
          <TheIcon icon="material-symbols:add" :size="18" class="mr-5" />新建分类
        </NButton>
      </div>
    </template>
    <!-- 表格 -->
    <CrudTable
      ref="$table"
      v-model:query-items="queryItems"
      :columns="columns"
      :get-data="api.getCategoryList"
    >
      <template #queryBar>
        <QueryBarItem label="分类名称" :label-width="80">
          <NInput
            v-model:value="queryItems.name"
            clearable
            type="text"
            placeholder="请输入分类名称"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="状态" :label-width="80">
          <NSelect
            v-model:value="queryItems.is_active"
            clearable
            placeholder="全部"
            :options="[
              { label: '启用', value: true },
              { label: '禁用', value: false },
            ]"
            style="width: 120px"
          />
        </QueryBarItem>
      </template>
    </CrudTable>

    <!-- 新增/编辑 弹窗 -->
    <CrudModal
      v-model:visible="modalVisible"
      :title="modalTitle"
      :loading="modalLoading"
      @save="handleSave"
    >
      <NForm
        ref="modalFormRef"
        label-placement="left"
        label-align="left"
        :label-width="100"
        :model="modalForm"
        :rules="categoryRules"
      >
        <NFormItem label="分类名称" path="name">
          <NInput v-model:value="modalForm.name" clearable placeholder="请输入分类名称" />
        </NFormItem>
        <NFormItem label="分类描述" path="description">
          <NInput v-model:value="modalForm.description" type="textarea" placeholder="请输入分类描述" :rows="3" />
        </NFormItem>
        <NFormItem label="图标" path="icon">
          <NInput v-model:value="modalForm.icon" clearable placeholder="请输入图标名称 (如: material-symbols:category)" />
        </NFormItem>
        <NFormItem label="图片URL" path="image_url">
          <div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap;">
            <NInput v-model:value="modalForm.image_url" clearable placeholder="请输入分类图片URL或选择本地文件" style="width: 320px;" />
            <input type="file" accept="image/*" @change="onImageFileChange" />
            <img v-if="modalForm.image_url" :src="modalForm.image_url" alt="预览" style="width: 80px; height: 60px; object-fit: cover; border-radius: 4px;" />
          </div>
        </NFormItem>
        <NFormItem label="是否启用" path="is_active">
          <NSwitch v-model:value="modalForm.is_active" />
        </NFormItem>
        <NFormItem label="排序" path="order">
          <NInputNumber v-model:value="modalForm.order" min="0"></NInputNumber>
        </NFormItem>
      </NForm>
    </CrudModal>
  </CommonPage>
</template>

