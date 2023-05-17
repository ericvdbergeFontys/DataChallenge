<script lang="ts">
import { 
    LogOutOutline as LogOutIcon 
} from '@vicons/ionicons5'

export default defineComponent({
  components: {
    LogOutIcon,
  },
  setup () {
    return {
        LogOutIcon
    }
  }
})
</script>

<template>
    <div class="header">
        <h1>Data Challenge - Semester 7</h1>
        <n-icon size="30" color="#0e7a0d">
            <log-out-icon />
        </n-icon>
    </div>
</template>

<style lang="scss" scoped>
.header {
    width: 100%;
    height: 55px;
    padding: 3px 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
</style>