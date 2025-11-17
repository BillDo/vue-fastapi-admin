<template>
  <div class="default-layout">
    <header class="header">
      <div class="container">
        <router-link to="/" class="logo">MyApp</router-link>
        <nav class="nav">
          <router-link to="/">Home</router-link>
          <router-link to="/about">About</router-link>
          <router-link v-if="!isLoggedIn" to="/login">Login</router-link>
          <router-link v-else to="/dashboard">Dashboard</router-link>
        </nav>
      </div>
    </header>
    <main class="main">
      <slot />
    </main>
    <footer class="footer">
      <div class="container">
        <p>&copy; 2025 MyApp. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useUserStore } from '@/store/user'

const userStore = useUserStore()
const isLoggedIn = computed(() => userStore.isLoggedIn)
</script>

<style scoped lang="scss">
.default-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;

  .header {
    background: white;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    padding: 1rem 0;

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo {
      font-size: 1.5rem;
      font-weight: bold;
      color: #18a058;
      text-decoration: none;
    }

    .nav {
      display: flex;
      gap: 2rem;

      a {
        color: #333;
        text-decoration: none;
        transition: color 0.3s;

        &:hover,
        &.router-link-active {
          color: #18a058;
        }
      }
    }
  }

  .main {
    flex: 1;
  }

  .footer {
    background: #333;
    color: white;
    padding: 2rem 0;
    text-align: center;
    margin-top: auto;

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }
  }
}
</style>

