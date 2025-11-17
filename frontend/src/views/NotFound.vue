<template>
  <div class="not-found">
    <div class="container">
      <h1>404</h1>
      <p>Page Not Found</p>
      <n-button type="primary" @click="$router.push('/')">
        Go Home
      </n-button>
    </div>
  </div>
</template>

<script setup>
import { NButton } from 'naive-ui'
</script>

<style scoped lang="scss">
.not-found {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  
  .container {
    text-align: center;
    
    h1 {
      font-size: 6rem;
      margin-bottom: 1rem;
      color: #18a058;
    }
    
    p {
      font-size: 1.5rem;
      margin-bottom: 2rem;
    }
  }
}
</style>

