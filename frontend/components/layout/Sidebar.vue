<template>
  <div>
    <img src="/beep.png" class="logo"/>
    <n-menu
        :inverted="false"
        :collapsed-width="64"
        :collapsed-icon-size="22"
        :options="menuOptions"
    />
  </div>    
</template>

<script setup lang="ts">
import { NIcon } from 'naive-ui'
import {
  Grid as DashboardIcon,
  BarChart as InsightsIcon,
  Cog as SettingsIcon,
  Shirt as ProductsIcon,
  BagCheck as OrdersIcon
} from '@vicons/ionicons5'

function renderIcon (icon: Component) {
  return () => h(NIcon, null, { default: () => h(icon) })
}

const menuOptions = [
  {
    label: 'Dashboard',
    key: 'dashboard',
    icon: renderIcon(DashboardIcon),
    // href: '/'
  },
  {
    label: () =>
      h(
      'a',
      {
        href: '/insights',
      },
      'Insights'
    ),
    key: 'insights',
    icon: renderIcon(InsightsIcon),
    href: '/insights'
  },
  {
    label: 'Products',
    key: 'products',
    icon: renderIcon(ProductsIcon)
  },
  {
    label: 'Orders',
    key: 'orders',
    icon: renderIcon(OrdersIcon)
  },
  {
    label: 'Settings',
    key: 'settings',
    icon: renderIcon(SettingsIcon)
  }
]
</script>

<style lang="scss">
.logo {
  width: 100%;
  object-fit: cover;
  margin-bottom: 10px;
}
</style>