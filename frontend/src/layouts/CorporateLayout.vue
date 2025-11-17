<template>
  <div class="corporate-layout">
    <header class="header" :class="{ sticky: isScrolled }">
      <div class="container">
        <router-link to="/" class="logo">
          <span>Company</span>
        </router-link>
        <nav class="nav">
          <router-link to="/about">{{ $t('nav.about') }}</router-link>
          <router-link to="/products">{{ $t('nav.products') }}</router-link>
          <router-link to="/services">{{ $t('nav.services') }}</router-link>
          <router-link to="/news">{{ $t('nav.news') }}</router-link>
          <router-link to="/contact">{{ $t('nav.contact') }}</router-link>
        </nav>
        <LanguageSwitcher />
      </div>
    </header>
    <main class="main">
      <slot />
    </main>
    <footer class="footer">
      <div class="container">
        <div class="footer-content">
          <div class="footer-section">
            <h3>{{ $t('nav.contact') }}</h3>
            <p><strong>{{ $t('contact.tel') }}:</strong> +886-2608-7707</p>
            <p><strong>{{ $t('contact.fax') }}:</strong> +886-2608-7705</p>
            <p><strong>{{ $t('contact.email') }}:</strong> sales@company.com</p>
          </div>
          <div class="footer-section">
            <h3>{{ $t('nav.about') }}</h3>
            <p>{{ $t('about.description') }}</p>
          </div>
          <div class="footer-section">
            <h3>{{ $t('nav.services') }}</h3>
            <p>{{ $t('services.description') }}</p>
          </div>
        </div>
        <div class="footer-bottom">
          <p>{{ $t('footer.copyright') }}</p>
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import LanguageSwitcher from '@/components/LanguageSwitcher.vue'

const isScrolled = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped lang="scss">
.corporate-layout {
  min-height: 100vh;
  display: flex;
  flex-direction: column;

  .header {
    background: white;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    padding: 1rem 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    transition: all 0.3s ease;

    &.sticky {
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .logo {
      font-size: 1.8rem;
      font-weight: bold;
      color: #1e3a8a;
      text-decoration: none;
      transition: color 0.3s;

      &:hover {
        color: #3b82f6;
      }
    }

    .nav {
      display: flex;
      gap: 2rem;
      align-items: center;

      a {
        color: #333;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.3s;
        position: relative;

        &:hover,
        &.router-link-active {
          color: #1e3a8a;
        }

        &.router-link-active::after {
          content: '';
          position: absolute;
          bottom: -8px;
          left: 0;
          right: 0;
          height: 2px;
          background: #1e3a8a;
        }
      }
    }
  }

  .main {
    flex: 1;
  }

  .footer {
    background: #1e293b;
    color: white;
    padding: 3rem 0 1rem;
    margin-top: 4rem;

    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }

    .footer-content {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 2rem;
      margin-bottom: 2rem;
    }

    .footer-section {
      h3 {
        font-size: 1.2rem;
        margin-bottom: 1rem;
        color: #60a5fa;
      }

      p {
        margin: 0.5rem 0;
        line-height: 1.6;
        opacity: 0.9;
      }
    }

    .footer-bottom {
      text-align: center;
      padding-top: 2rem;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      opacity: 0.8;
    }
  }
}

@media (max-width: 768px) {
  .corporate-layout {
    .header {
      .container {
        flex-wrap: wrap;
      }

      .nav {
        order: 3;
        width: 100%;
        margin-top: 1rem;
        gap: 1rem;
        flex-wrap: wrap;
      }
    }
  }
}
</style>

