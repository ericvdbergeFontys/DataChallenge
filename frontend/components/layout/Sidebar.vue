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
  BarChart,
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
          route: to,
          params: {
            lang: 'en-US'
          }
        }
    },
    label
  )
}

const menuOptions = [
  {
    label: () => renderLink("index", "Dashboard"),
    key: 'dashboard',
    icon: renderIcon(Grid),
    // href: '/'
  },
  {
    label: () => renderLink("insights", "Insights"),
    key: 'insights',
    icon: renderIcon(BarChart),
    // href: '/insights'
  },
  {
    label: () => renderLink("products", "Products"),
    key: 'products',
    icon: renderIcon(Shirt)
  },
  {
    label: () => renderLink("orders", "Orders"),
    key: 'orders',
    icon: renderIcon(BagCheck)
  },
  {
    label: () => renderLink("settings", "Settings"),
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