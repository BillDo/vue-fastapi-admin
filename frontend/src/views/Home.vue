<template>
  <CorporateLayout>
    <!-- Hero Section -->
    <section class="hero">
      <div class="container">
        <h1>{{ $t('home.hero.title') }}</h1>
        <p class="subtitle">{{ $t('home.hero.subtitle') }}</p>
        <div class="hero-content">
          <div class="hero-text">
            <p>
              A professional and diversified enterprise specializing in lubricants, 
              precision adhesives, thermal conductive materials, and electronic auxiliary consumables.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Core Values Section -->
    <section class="core-values">
      <div class="container">
        <h2>{{ $t('home.coreValues.title') }}</h2>
        <p class="section-description">{{ $t('home.coreValues.description') }}</p>
        <div class="values-grid">
          <div class="value-card" v-for="value in coreValues" :key="value.title">
            <div class="value-icon">
              <component :is="value.icon" />
            </div>
            <h3>{{ value.title }}</h3>
            <p>{{ value.description }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Services Section -->
    <section class="services-preview">
      <div class="container">
        <h2>{{ $t('home.services.title') }}</h2>
        <p class="section-description">{{ $t('home.services.description') }}</p>
        <div class="services-grid">
          <div class="service-item" v-for="service in services" :key="service.title">
            <h3>{{ service.title }}</h3>
            <p>{{ service.description }}</p>
          </div>
        </div>
        <div class="cta">
          <n-button type="primary" size="large" @click="$router.push('/services')">
            {{ $t('nav.services') }}
          </n-button>
        </div>
      </div>
    </section>
  </CorporateLayout>
</template>

<script setup>
import { ref } from 'vue'
import CorporateLayout from '@/layouts/CorporateLayout.vue'
import { NButton } from 'naive-ui'
import IconMdiTarget from '~icons/mdi/target'
import IconMdiLightbulbOn from '~icons/mdi/lightbulb-on'
import IconMdiHandshake from '~icons/mdi/handshake'

const coreValues = ref([
  {
    title: 'Excellence',
    description: 'Committed to delivering the highest quality products and services',
    icon: IconMdiTarget,
  },
  {
    title: 'Innovation',
    description: 'Continuously developing new solutions to meet evolving market needs',
    icon: IconMdiLightbulbOn,
  },
  {
    title: 'Partnership',
    description: 'Building long-term relationships with our clients based on trust',
    icon: IconMdiHandshake,
  },
])

const services = ref([
  {
    title: 'Comprehensive Project Planning',
    description: 'End-to-end project management and planning services',
  },
  {
    title: 'Technical Services',
    description: 'Professional technical support and consulting',
  },
  {
    title: 'Product Development',
    description: 'Custom product development and R&D services',
  },
])
</script>

<style scoped lang="scss">
.hero {
  background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
  color: white;
  padding: 5rem 20px;
  text-align: center;

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    font-weight: 700;
  }

  .subtitle {
    font-size: 1.5rem;
    margin-bottom: 2rem;
    opacity: 0.9;
  }

  .hero-content {
    max-width: 800px;
    margin: 0 auto;

    .hero-text {
      font-size: 1.1rem;
      line-height: 1.8;
      opacity: 0.95;
    }
  }
}

.core-values {
  padding: 4rem 20px;
  background: #f8fafc;

  .container {
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
  }

  h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #1e3a8a;
  }

  .section-description {
    font-size: 1.2rem;
    color: #64748b;
    margin-bottom: 3rem;
  }

  .values-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-top: 3rem;
  }

  .value-card {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;

    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
    }

    .value-icon {
      font-size: 3rem;
      color: #3b82f6;
      margin-bottom: 1rem;
    }

    h3 {
      font-size: 1.5rem;
      margin-bottom: 1rem;
      color: #1e3a8a;
    }

    p {
      color: #64748b;
      line-height: 1.6;
    }
  }
}

.services-preview {
  padding: 4rem 20px;
  background: white;

  .container {
    max-width: 1200px;
    margin: 0 auto;
    text-align: center;
  }

  h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #1e3a8a;
  }

  .section-description {
    font-size: 1.2rem;
    color: #64748b;
    margin-bottom: 3rem;
  }

  .services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    margin-bottom: 3rem;
  }

  .service-item {
    padding: 2rem;
    background: #f8fafc;
    border-radius: 8px;
    text-align: left;

    h3 {
      font-size: 1.3rem;
      margin-bottom: 1rem;
      color: #1e3a8a;
    }

    p {
      color: #64748b;
      line-height: 1.6;
    }
  }

  .cta {
    margin-top: 2rem;
  }
}

@media (max-width: 768px) {
  .hero h1 {
    font-size: 2rem;
  }

  .hero .subtitle {
    font-size: 1.2rem;
  }
}
</style>
