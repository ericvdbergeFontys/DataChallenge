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
    // width: 100%;
    height: 55px;
    box-sizing: border-box;
    // padding: 3px 20px;
    // display: flex;
    // justify-content: space-between;
    // align-items: center;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
    padding: 0 20px !important;
    background: #333;
    
    > * {
      display: flex;
      gap: 10px;
      color: white;
      text-decoration: none;
    }
}
</style>