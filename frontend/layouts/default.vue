<template>
    <n-layout has-sider content-style="height: 100vh">
      <n-layout-sider
          collapse-mode="transform"
          :collapsed-width="80"
          width="240"
          show-trigger="arrow-circle"
          bordered
      >
        <LayoutSidebar/>
      </n-layout-sider>
      <n-layout content-style="display: flex; flex-direction: column">
        <n-layout-header bordered>
          <LayoutHeader />
        </n-layout-header>
        <n-layout-content content-style="padding: 24px; flex: 1">
          <NuxtPage/>
        </n-layout-content>
        <n-layout-footer bordered>
          footer
        </n-layout-footer>
      </n-layout>
    </n-layout>
</template>