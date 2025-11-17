<template>
  <div class="login">
    <div class="login-container">
      <n-card class="login-card">
        <template #header>
          <h2>Sign In</h2>
        </template>
        <n-form ref="formRef" :model="formData" :rules="rules">
          <n-form-item path="username" label="Username">
            <n-input v-model:value="formData.username" placeholder="Enter username" />
          </n-form-item>
          <n-form-item path="password" label="Password">
            <n-input
              v-model:value="formData.password"
              type="password"
              placeholder="Enter password"
              show-password-on="click"
            />
          </n-form-item>
          <n-form-item>
            <n-button
              type="primary"
              block
              size="large"
              :loading="loading"
              @click="handleLogin"
            >
              Sign In
            </n-button>
          </n-form-item>
        </n-form>
        <div class="links">
          <router-link to="/">Back to Home</router-link>
        </div>
      </n-card>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useUserStore } from '@/store/user'
import { NCard, NForm, NFormItem, NInput, NButton, useMessage } from 'naive-ui'

const router = useRouter()
const route = useRoute()
const userStore = useUserStore()
const message = useMessage()

const formRef = ref(null)
const loading = ref(false)

const formData = ref({
  username: '',
  password: '',
})

const rules = {
  username: {
    required: true,
    message: 'Please enter username',
    trigger: 'blur',
  },
  password: {
    required: true,
    message: 'Please enter password',
    trigger: 'blur',
  },
}

const handleLogin = async () => {
  try {
    await formRef.value?.validate()
    loading.value = true
    
    await userStore.login(formData.value)
    message.success('Login successful')
    
    const redirect = route.query.redirect || '/dashboard'
    router.push(redirect)
  } catch (error) {
    console.error('Login error:', error)
    message.error(error.message || 'Login failed')
  } finally {
    loading.value = false
  }
}
</script>

<style scoped lang="scss">
.login {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;

  .login-container {
    width: 100%;
    max-width: 400px;
  }

  .login-card {
    :deep(.n-card-header) {
      text-align: center;
      
      h2 {
        margin: 0;
        font-size: 2rem;
      }
    }
  }

  .links {
    text-align: center;
    margin-top: 1rem;
    
    a {
      color: #18a058;
      text-decoration: none;
      
      &:hover {
        text-decoration: underline;
      }
    }
  }
}
</style>

