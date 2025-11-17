<template>
  <CorporateLayout>
    <div class="news-page">
      <div class="container">
        <h1>{{ $t('news.title') }}</h1>
        <p class="description">{{ $t('news.description') }}</p>

        <div class="news-list">
          <n-card v-for="news in newsItems" :key="news.id" class="news-card">
            <div class="news-date">{{ news.date }}</div>
            <h3>{{ news.title }}</h3>
            <p>{{ news.description }}</p>
          </n-card>
        </div>
      </div>
    </div>
  </CorporateLayout>
</template>

<script setup>
import { ref } from 'vue'
import CorporateLayout from '@/layouts/CorporateLayout.vue'
import { NCard } from 'naive-ui'

const newsItems = ref([
  {
    id: 1,
    date: '2025-01-15',
    title: 'New Product Launch',
    description: 'We are excited to announce the launch of our new line of thermal conductive materials.',
  },
  {
    id: 2,
    date: '2025-01-10',
    title: 'Industry Conference 2025',
    description: 'Join us at the upcoming industry conference to learn about the latest innovations.',
  },
  {
    id: 3,
    date: '2024-12-20',
    title: 'Year-End Summary',
    description: 'A look back at our achievements and milestones throughout 2024.',
  },
])
</script>

<style scoped lang="scss">
.news-page {
  padding: 4rem 20px;
  min-height: 60vh;

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  h1 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: #1e3a8a;
    text-align: center;
  }

  .description {
    text-align: center;
    font-size: 1.2rem;
    color: #64748b;
    margin-bottom: 3rem;
  }

  .news-list {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }

  .news-card {
    .news-date {
      color: #3b82f6;
      font-size: 0.9rem;
      margin-bottom: 0.5rem;
      font-weight: 500;
    }

    h3 {
      color: #1e3a8a;
      margin-bottom: 1rem;
      font-size: 1.5rem;
    }

    p {
      color: #64748b;
      line-height: 1.6;
    }
  }
}
</style>

