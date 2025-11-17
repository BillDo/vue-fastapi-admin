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

defineOptions({ name: '产品管理' })

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
  name: 'Product',
  initForm: { order: 0, is_active: true, features: [] },
  doCreate: api.createProduct,
  doUpdate: api.updateProduct,
  doDelete: api.deleteProduct,
  refresh: () => $table.value?.handleSearch(),
})

const featureInput = ref('')
const categoryOptions = ref([])

onMounted(() => {
  $table.value?.handleSearch()
  loadCategories()
})

const loadCategories = async () => {
  try {
    const response = await api.getActiveCategories()
    if (response.data) {
      categoryOptions.value = response.data.map((cat) => ({
        label: cat.name,
        value: cat.id,
      }))
      // Add empty option
      categoryOptions.value.unshift({ label: '无分类', value: null })
    }
  } catch (error) {
    console.error('Failed to load categories:', error)
  }
}

const productRules = {
  name: [
    {
      required: true,
      message: '请输入产品名称',
      trigger: ['input', 'blur', 'change'],
    },
  ],
}

function addProduct() {
  featureInput.value = ''
  loadCategories()
  handleAdd()
}

function addFeature() {
  if (featureInput.value && featureInput.value.trim()) {
    if (!modalForm.value.features) {
      modalForm.value.features = []
    }
    modalForm.value.features.push(featureInput.value.trim())
    featureInput.value = ''
  }
}

function removeFeature(index) {
  modalForm.value.features.splice(index, 1)
}

const columns = [
  {
    title: '产品名称',
    key: 'name',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: '分类',
    key: 'category',
    align: 'center',
    width: '150',
    render(row) {
      return row.category ? h(NTag, { type: 'info', size: 'small' }, { default: () => row.category }) : '-'
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
            onClick: () => {
              featureInput.value = ''
              loadCategories()
              handleEdit(row)
            },
            },
            {
              default: () => '编辑',
              icon: renderIcon('material-symbols:edit', { size: 16 }),
            }
          ),
          [[vPermission, 'post/api/v1/product/update']]
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
                [[vPermission, 'delete/api/v1/product/delete']]
              ),
            default: () => h('div', {}, '确定删除该产品吗?'),
          }
        ),
      ]
    },
  },
]
</script>

<template>
  <!-- 业务页面 -->
  <CommonPage show-footer title="产品列表">
    <template #action>
      <div>
        <NButton
          v-permission="'post/api/v1/product/create'"
          class="float-right mr-15"
          type="primary"
          @click="addProduct"
        >
          <TheIcon icon="material-symbols:add" :size="18" class="mr-5" />新建产品
        </NButton>
      </div>
    </template>
    <!-- 表格 -->
    <CrudTable
      ref="$table"
      v-model:query-items="queryItems"
      :columns="columns"
      :get-data="api.getProductList"
    >
      <template #queryBar>
        <QueryBarItem label="产品名称" :label-width="80">
          <NInput
            v-model:value="queryItems.name"
            clearable
            type="text"
            placeholder="请输入产品名称"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="分类" :label-width="80">
          <NInput
            v-model:value="queryItems.category"
            clearable
            type="text"
            placeholder="请输入产品分类"
            @keypress.enter="$table?.handleSearch()"
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
        :rules="productRules"
      >
        <NFormItem label="产品名称" path="name">
          <NInput v-model:value="modalForm.name" clearable placeholder="请输入产品名称" />
        </NFormItem>
        <NFormItem label="产品分类" path="category_id">
          <NSelect
            v-model:value="modalForm.category_id"
            :options="categoryOptions"
            placeholder="请选择产品分类"
            clearable
            filterable
          />
        </NFormItem>
        <NFormItem label="分类(兼容)" path="category" v-if="false">
          <NInput v-model:value="modalForm.category" clearable placeholder="自动填充" />
        </NFormItem>
        <NFormItem label="产品描述" path="description">
          <NInput v-model:value="modalForm.description" type="textarea" placeholder="请输入产品描述" :rows="4" />
        </NFormItem>
        <NFormItem label="图片URL" path="image_url">
          <NInput v-model:value="modalForm.image_url" clearable placeholder="请输入产品图片URL" />
        </NFormItem>
        <NFormItem label="产品特性" path="features">
          <div style="width: 100%">
            <div style="display: flex; gap: 8px; margin-bottom: 8px">
              <NInput
                v-model:value="featureInput"
                placeholder="输入特性后按回车添加"
                @keypress.enter="addFeature"
                style="flex: 1"
              />
              <NButton type="primary" @click="addFeature">添加</NButton>
            </div>
            <div v-if="modalForm.features && modalForm.features.length > 0" style="display: flex; flex-wrap: wrap; gap: 8px">
              <NTag
                v-for="(feature, index) in modalForm.features"
                :key="index"
                closable
                @close="removeFeature(index)"
              >
                {{ feature }}
              </NTag>
            </div>
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

