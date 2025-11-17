<template>
  <div class="dashboard">
    <div class="header">
      <div class="container">
        <h1>Dashboard</h1>
        <n-button @click="handleLogout">Logout</n-button>
      </div>
    </div>
    
    <div class="container">
      <n-card v-if="userInfo">
        <template #header>
          <h2>Welcome, {{ userInfo.username || 'User' }}!</h2>
        </template>
        <div class="info">
          <p><strong>Email:</strong> {{ userInfo.email || 'N/A' }}</p>
          <p><strong>User ID:</strong> {{ userInfo.id || 'N/A' }}</p>
        </div>
      </n-card>

      <div class="cards">
        <n-card title="Overview">
          <p>This is your personal dashboard. More features coming soon!</p>
        </n-card>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/store/user'
import { NCard, NButton, useMessage } from 'naive-ui'

const router = useRouter()
const userStore = useUserStore()
const message = useMessage()

const userInfo = ref(null)

onMounted(async () => {
  try {
    if (userStore.userInfo) {
      userInfo.value = userStore.userInfo
    } else {
      userInfo.value = await userStore.getUserInfo()
    }
  } catch (error) {
    console.error('Failed to load user info:', error)
    message.error('Failed to load user information')
  }
})

const handleLogout = () => {
  userStore.logout()
  message.success('Logged out successfully')
  router.push('/')
}
</script>

<style scoped lang="scss">
.dashboard {
  min-height: 100vh;
  background-color: #f5f5f5;

  .header {
    background: white;
    padding: 1rem 0;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    h1 {
      margin: 0;
    }
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
  }

  .info {
    margin-top: 1rem;
    
    p {
      margin: 0.5rem 0;
    }
  }

  .cards {
    margin-top: 2rem;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
  }
}
</style>

