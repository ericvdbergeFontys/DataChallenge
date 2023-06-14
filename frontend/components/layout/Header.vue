<template>
    <n-layout-header bordered>
      <NuxtLink to="/">
        <img style="width: 30px" src="/icon.png"/>
        <h2>Reviewify</h2>
      </NuxtLink>
      <NuxtLink to="/dashboard">Login</NuxtLink>
    </n-layout-header>
</template>

<style lang="scss" scoped>
.n-layout-header {
    box-sizing: border-box;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    padding: 20px 20px !important;
    background: #333;
    
    > * {
      display: flex;
      gap: 10px;
      color: white;
      text-decoration: none;
    }
}
</style>