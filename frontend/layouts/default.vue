<template>
    <n-layout content-style="height: 100vh">
        <n-layout-header>
          <LayoutHeader/>
        </n-layout-header>
        <n-layout-content content-style="padding: 24px; flex: 1">
          <NuxtPage/>
        </n-layout-content>
    </n-layout>
</template>

<style scoped>
.n-layout-header * {
  display: flex;
  align-items: center;
  gap: 10px;
}

h2, a {
  color: white;
  text-decoration: none;
}
</style>