<template>
  <div class="sidebar">
    <n-menu
        :inverted="false"
        :collapsed-width="64"
        :collapsed-icon-size="22"
        :options="menuOptions"
    />
  </div>    
</template>

<script setup>
import { NIcon } from 'naive-ui'
import { RouterLink } from 'vue-router'
import {
  Grid,
  Cog,
  Shirt,
  BagCheck
} from '@vicons/ionicons5'

function renderIcon (icon) {
  return () => h(NIcon, null, { default: () => h(icon) })
}

function renderLink (to, label) {
  return h(
      RouterLink,
      {
          to: {
            name: to,
          }
      },
      { default: () => label }
    )
}

const menuOptions = [
  {
    label: () => renderLink("dashboard", "Dashboard"),
    key: 'dashboard',
    icon: renderIcon(Grid),
    // href: '/'
  },
  {
    label: () => renderLink("dashboard-products", "Products"),
    key: 'products',
    icon: renderIcon(Shirt)
  },
  {
    label: () => renderLink("dashboard-orders", "Orders"),
    key: 'orders',
    icon: renderIcon(BagCheck)
  },
  {
    label: () => renderLink("dashboard-settings", "Settings"),
    key: 'settings',
    icon: renderIcon(Cog)
  }
]
</script>

<style lang="scss">
.sidebar {
  padding: 50px 0px;
}
</style>