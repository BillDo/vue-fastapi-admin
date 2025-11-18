<script setup>
import { h, onMounted, ref, resolveDirective, withDirectives } from 'vue'
import { NButton, NForm, NFormItem, NInput, NPopconfirm } from 'naive-ui'

import CommonPage from '@/components/page/CommonPage.vue'
import QueryBarItem from '@/components/query-bar/QueryBarItem.vue'
import CrudModal from '@/components/table/CrudModal.vue'
import CrudTable from '@/components/table/CrudTable.vue'
import TheIcon from '@/components/icon/TheIcon.vue'

import { renderIcon } from '@/utils'
import { useCRUD } from '@/composables'
// import { loginTypeMap, loginTypeOptions } from '@/constant/data'
import api from '@/api'

defineOptions({ name: 'API管理' })

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
  name: 'API',
  initForm: {},
  doCreate: api.createApi,
  doUpdate: api.updateApi,
  doDelete: api.deleteApi,
  refresh: () => $table.value?.handleSearch(),
})

onMounted(() => {
  $table.value?.handleSearch()
})

async function handleRefreshApi() {
  await $dialog.confirm({
    title: 'hint',
    type: 'warning',
    content: 'This operation will update routes based on the backend app.routes. Are you sure you want to continue refreshing the API?',
    async confirm() {
      await api.refreshApi()
      $message.success('Refresh completed')
      $table.value?.handleSearch()
    },
  })
}

const addAPIRules = {
  path: [
    {
      required: true,
      message: 'Please enter the API path',
      trigger: ['input', 'blur', 'change'],
    },
  ],
  method: [
    {
      required: true,
      message: 'Please enter the request method',
      trigger: ['input', 'blur', 'change'],
    },
  ],
  summary: [
    {
      required: true,
      message: 'Please enter the API summary',
      trigger: ['input', 'blur', 'change'],
    },
  ],
  tags: [
    {
      required: true,
      message: 'Please enter Tags',
      trigger: ['input', 'blur', 'change'],
    },
  ],
}

const columns = [
  {
    title: 'API Path',
    key: 'path',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: 'Request Method',
    key: 'method',
    align: 'center',
    width: 'auto',
    ellipsis: { tooltip: true },
  },
  {
    title: 'API Summary',
    key: 'summary',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: 'Tags',
    key: 'tags',
    width: 'auto',
    align: 'center',
    ellipsis: { tooltip: true },
  },
  {
    title: 'Actions',
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
              style: 'margin-right: 8px;',
              onClick: () => {
                handleEdit(row)
                modalForm.value.roles = row.roles.map((e) => (e = e.id))
              },
            },
            {
              default: () => 'Edit',
              icon: renderIcon('material-symbols:edit', { size: 16 }),
            }
          ),
          [[vPermission, 'post/api/v1/api/update']]
        ),
        h(
          NPopconfirm,
          {
            onPositiveClick: () => handleDelete({ api_id: row.id }, false),
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
                    style: 'margin-right: 8px;',
                  },
                  {
                    default: () => 'Delete',
                    icon: renderIcon('material-symbols:delete-outline', { size: 16 }),
                  }
                ),
                [[vPermission, 'delete/api/v1/api/delete']]
              ),
            default: () => h('div', {}, 'Are you sure you want to delete this API?'),
          }
        ),
      ]
    },
  },
]
</script>

<template>
  <!-- 业务页面 -->
  <CommonPage show-footer title="API列表">
    <template #action>
      <div>
        <NButton
          v-permission="'post/api/v1/api/create'"
          class="float-right mr-15"
          type="primary"
          @click="handleAdd"
        >
          <TheIcon icon="material-symbols:add" :size="18" class="mr-5" />New API
        </NButton>
        <NButton
          v-permission="'post/api/v1/api/refresh'"
          class="float-right mr-15"
          type="warning"
          @click="handleRefreshApi"
        >
          <TheIcon icon="material-symbols:refresh" :size="18" class="mr-5" />Refresh API
        </NButton>
      </div>
    </template>
    <!-- 表格 -->
    <CrudTable
      ref="$table"
      v-model:query-items="queryItems"
      :columns="columns"
      :get-data="api.getApis"
    >
      <template #queryBar>
        <QueryBarItem label="Path" :label-width="40">
          <NInput
            v-model:value="queryItems.path"
            clearable
            type="text"
            placeholder="Please enter the API path"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="API Summary" :label-width="70">
          <NInput
            v-model:value="queryItems.summary"
            clearable
            type="text"
            placeholder="Please enter the API summary"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
        <QueryBarItem label="Tags" :label-width="40">
          <NInput
            v-model:value="queryItems.tags"
            clearable
            type="text"
            placeholder="Please enter the API tags"
            @keypress.enter="$table?.handleSearch()"
          />
        </QueryBarItem>
      </template>
    </CrudTable>

    <!-- New/Edit Modal -->
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
        :label-width="80"
        :model="modalForm"
        :rules="addAPIRules"
      >
        <NFormItem label="API Name" path="path">
          <NInput v-model:value="modalForm.path" clearable placeholder="Please enter the API path" />
        </NFormItem>
        <NFormItem label="Method" path="method">
          <NInput v-model:value="modalForm.method" clearable placeholder="Please enter the method" />
        </NFormItem>
        <NFormItem label="API Summary" path="summary">
          <NInput v-model:value="modalForm.summary" clearable placeholder="Please enter the API summary" />
        </NFormItem>
        <NFormItem label="Tags" path="tags">
          <NInput v-model:value="modalForm.tags" clearable placeholder="Please enter the API tags" />
        </NFormItem>
      </NForm>
    </CrudModal>
  </CommonPage>
</template>
