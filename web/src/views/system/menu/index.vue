<script setup>
import { h, onMounted, ref, resolveDirective, withDirectives } from 'vue'
import {
  NButton,
  NForm,
  NFormItem,
  NInput,
  NInputNumber,
  NPopconfirm,
  NSwitch,
  NTreeSelect,
  NRadio,
  NRadioGroup,
  NTag,
} from 'naive-ui'

import CommonPage from '@/components/page/CommonPage.vue'
import CrudModal from '@/components/table/CrudModal.vue'
import CrudTable from '@/components/table/CrudTable.vue'
import IconPicker from '@/components/icon/IconPicker.vue'
import TheIcon from '@/components/icon/TheIcon.vue'

import { formatDate, renderIcon } from '@/utils'
import { useCRUD } from '@/composables'
import api from '@/api'

defineOptions({ name: 'Menu Management' })

const $table = ref(null)
const queryItems = ref({})
const vPermission = resolveDirective('permission')

// Form initial content
const initForm = {
  order: 1,
  keepalive: true,
}

const {
  modalVisible,
  modalTitle,
  modalLoading,
  handleAdd,
  handleDelete,
  handleEdit,
  handleSave,
  modalForm,
  modalFormRef,
} = useCRUD({
  name: 'Menu',
  initForm,
  doCreate: api.createMenu,
  doDelete: api.deleteMenu,
  doUpdate: api.updateMenu,
  refresh: () => $table.value?.handleSearch(),
})

onMounted(() => {
  $table.value?.handleSearch()
  getTreeSelect()
})

// Whether to show "Menu Type"
const showMenuType = ref(false)
const menuOptions = ref([])

const columns = [
  { title: 'ID', key: 'id', width: 50, ellipsis: { tooltip: true }, align: 'center' },
  { title: 'Menu Name', key: 'name', width: 80, ellipsis: { tooltip: true }, align: 'center' },
  {
    title: 'Menu Type',
    key: 'menu_type',
    width: 80,
    align: 'center',
    ellipsis: { tooltip: true },
    render(row) {
      let round = false
      let bordered = false
      if (row.menu_type === 'catalog') {
        bordered = true
        round = false
      } else if (row.menu_type === 'menu') {
        bordered = false
        round = true
      }
      return h(
        NTag,
        { type: 'primary', round: round, bordered: bordered },
        { default: () => (row.menu_type === 'catalog' ? 'Catalog' : 'Menu') }
      )
    },
  },
  {
    title: 'Icon',
    key: 'icon',
    width: 40,
    align: 'center',
    render(row) {
      return h(TheIcon, { icon: row.icon, size: 20 })
    },
  },
  { title: 'Order', key: 'order', width: 40, ellipsis: { tooltip: true }, align: 'center' },
  { title: 'Access Path', key: 'path', width: 80, ellipsis: { tooltip: true }, align: 'center' },
  { title: 'Redirect Path', key: 'redirect', width: 80, ellipsis: { tooltip: true }, align: 'center' },
  { title: 'Component Path', key: 'component', width: 80, ellipsis: { tooltip: true }, align: 'center' },
  {
    title: 'Keepalive',
    key: 'keepalive',
    width: 40,
    align: 'center',
    render(row) {
      return h(NSwitch, {
        size: 'small',
        rubberBand: false,
        value: row.keepalive,
        onUpdateValue: () => handleUpdateKeepalive(row),
      })
    },
  },
  {
    title: 'Hidden',
    key: 'is_hidden',
    width: 40,
    align: 'center',
    render(row) {
      return h(NSwitch, {
        size: 'small',
        rubberBand: false,
        value: row.is_hidden,
        onUpdateValue: () => handleUpdateHidden(row),
      })
    },
  },
  {
    title: 'Created Date',
    key: 'created_at',
    width: 80,
    align: 'center',
    render(row) {
      return h('span', formatDate(row.created_at))
    },
  },
  {
    title: 'Actions',
    key: 'actions',
    width: 120,
    align: 'center',
    fixed: 'right',
    render(row) {
      return [
        withDirectives(
          h(
            NButton,
            {
              size: 'tiny',
              quaternary: true,
              type: 'primary',
              style: `display: ${row.children && row.menu_type !== 'menu' ? '' : 'none'};`,
              onClick: () => {
                initForm.parent_id = row.id
                initForm.menu_type = 'menu'
                showMenuType.value = false
                handleAdd()
              },
            },
            { default: () => 'Submenu', icon: renderIcon('material-symbols:add', { size: 16 }) }
          ),
          [[vPermission, 'post/api/v1/menu/create']]
        ),
        withDirectives(
          h(
            NButton,
            {
              size: 'tiny',
              quaternary: true,
              type: 'info',
              onClick: () => {
                showMenuType.value = false
                handleEdit(row)
              },
            },
            {
              default: () => 'Edit',
              icon: renderIcon('material-symbols:edit-outline', { size: 16 }),
            }
          ),
          [[vPermission, 'post/api/v1/menu/update']]
        ),
        h(
          NPopconfirm,
          {
            onPositiveClick: () => handleDelete({ id: row.id }, false),
          },
          {
            trigger: () =>
              withDirectives(
                h(
                  NButton,
                  {
                    size: 'tiny',
                    quaternary: true,
                    type: 'error',
                    style: `display: ${row.children && row.children.length > 0 ? 'none' : ''};`, // Submenus cannot be deleted
                  },
                  {
                    default: () => 'Delete',
                    icon: renderIcon('material-symbols:delete-outline', { size: 16 }),
                  }
                ),
                [[vPermission, 'delete/api/v1/menu/delete']]
              ),
            default: () => h('div', {}, 'Are you sure you want to delete this menu?'),
          }
        ),
      ]
    },
  },
]
// Modify whether keepalive is enabled
async function handleUpdateKeepalive(row) {
  if (!row.id) return
  row.publishing = true
  row.keepalive = row.keepalive === false ? true : false
  await api.updateMenu(row)
  row.publishing = false
  $message?.success(row.keepalive ? 'Enabled' : 'Disabled')
}

// Modify whether hidden
async function handleUpdateHidden(row) {
  if (!row.id) return
  row.publishing = true
  row.is_hidden = row.is_hidden === false ? true : false
  await api.updateMenu(row)
  row.publishing = false
  $message?.success(row.is_hidden ? 'Hidden' : 'Unhidden')
}

// Add new menu (optional directory)
function handleClickAdd() {
  initForm.parent_id = 0
  initForm.menu_type = 'catalog'
  initForm.is_hidden = false
  initForm.order = 1
  initForm.keepalive = true
  showMenuType.value = true
  handleAdd()
}

async function getTreeSelect() {
  const { data } = await api.getMenus()
  const menu = { id: 0, name: 'Root Directory', children: [] }
  menu.children = data
  menuOptions.value = [menu]
}
</script>

<template>
  <!-- Business Page -->
  <CommonPage show-footer title="Menu List">
    <template #action>
      <NButton v-permission="'post/api/v1/menu/create'" type="primary" @click="handleClickAdd">
        <TheIcon icon="material-symbols:add" :size="18" class="mr-5" />New Root Menu
      </NButton>
    </template>

    <!-- Table -->
    <CrudTable
      ref="$table"
      v-model:query-items="queryItems"
      :is-pagination="false"
      :columns="columns"
      :get-data="api.getMenus"
      :single-line="true"
    >
    </CrudTable>

    <!-- Add/Edit/View Modal -->
    <CrudModal
      v-model:visible="modalVisible"
      :title="modalTitle"
      :loading="modalLoading"
      @save="handleSave(getTreeSelect)"
    >
      <!-- Form -->
      <NForm
        ref="modalFormRef"
        label-placement="left"
        label-align="left"
        :label-width="80"
        :model="modalForm"
      >
        <NFormItem label="Menu Type" path="menu_type">
          <NRadioGroup v-model:value="modalForm.menu_type">
            <NRadio label="Table of contents" value="catalog" />
            <NRadio label="Menu" value="menu" />
          </NRadioGroup>
        </NFormItem>
        <NFormItem label="Parent Menu" path="parent_id">
          <NTreeSelect
            v-model:value="modalForm.parent_id"
            key-field="id"
            label-field="name"
            :options="menuOptions"
            default-expand-all="true"
          />
        </NFormItem>
        <NFormItem
          label="Menu Name"
          path="name"
          :rule="{
            required: true,
            message: 'Please enter a unique menu name',
            trigger: ['input', 'blur'],
          }"
        >
          <NInput v-model:value="modalForm.name" placeholder="Please enter a unique menu name" />
        </NFormItem>
        <NFormItem
          label="Access Path"
          path="path"
          :rule="{
            required: true,
            message: 'Please enter the access path',
            trigger: ['blur'],
          }"
        >
          <NInput v-model:value="modalForm.path" placeholder="Please enter the access path" />
        </NFormItem>
        <NFormItem v-if="modalForm.menu_type === 'menu'" label="Component Path" path="component">
          <NInput
            v-model:value="modalForm.component"
            placeholder="Please enter the component path, e.g., /system/user"
          />
        </NFormItem>
        <NFormItem label="Redirect Path" path="redirect">
          <NInput
            v-model:value="modalForm.redirect"
            :disabled="modalForm.parent_id !== 0"
            :placeholder="
              modalForm.parent_id !== 0 ? 'Only first-level menus can set redirect paths' : 'Please enter the redirect path'
            "
          />
        </NFormItem>
        <NFormItem label="Menu Icon" path="icon">
          <IconPicker v-model:value="modalForm.icon" />
        </NFormItem>
        <NFormItem label="Display Order" path="order">
          <NInputNumber v-model:value="modalForm.order" :min="1" />
        </NFormItem>
        <NFormItem label="Hidden" path="is_hidden">
          <NSwitch v-model:value="modalForm.is_hidden" />
        </NFormItem>
        <NFormItem label="KeepAlive" path="keepalive">
          <NSwitch v-model:value="modalForm.keepalive" />
        </NFormItem>
      </NForm>
    </CrudModal>
  </CommonPage>
</template>
