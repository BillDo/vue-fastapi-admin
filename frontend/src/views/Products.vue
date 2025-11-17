<template>
  <CorporateLayout>
    <div class="products-page">
      <div class="container">
        <h1>{{ $t('products.title') }}</h1>
        <p class="description">{{ $t('products.description') }}</p>

        <!-- Categories Grid -->
        <n-spin :show="loading">
          <div class="categories-grid" v-if="categories.length > 0">
            <router-link
              v-for="category in categories"
              :key="category.id"
              class="category-link"
              :to="{ name: 'CategoryProducts', params: { categoryId: category.id } }"
            >
              <n-card class="category-card">
                <template #header v-if="category.image_url">
                  <div class="product-image">
                    <img :src="category.image_url" :alt="category.name" />
                  </div>
                </template>
                <h3>{{ category.name }}</h3>
                <p class="category-desc" v-if="category.description">{{ category.description }}</p>
              </n-card>
            </router-link>
          </div>
          <div v-else-if="!loading" class="empty-state">
            <n-empty description="No categories available">
              <template #icon>
                <IconMdiPackageVariant />
              </template>
            </n-empty>
          </div>
        </n-spin>
      </div>
    </div>
  </CorporateLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import CorporateLayout from '@/layouts/CorporateLayout.vue'
import { NCard, NSpin, NEmpty } from 'naive-ui'
import api from '@/api'
import IconMdiPackageVariant from '~icons/mdi/package-variant'

const categories = ref([])
const loading = ref(true)

const loadCategories = async () => {
  try {
    loading.value = true
    const response = await api.getActiveCategories()
    console.log('Categories API response:', response) // Debug log
    
    // The interceptor returns { code, msg, data }
    // where data is the array of categories
    if (response && response.data && Array.isArray(response.data)) {
      categories.value = response.data
      console.log('Categories loaded:', categories.value.length) // Debug log
    } else {
      categories.value = []
      console.warn('No categories data in response or invalid format:', response)
    }
  } catch (error) {
    console.error('Failed to load categories:', error)
    categories.value = []
  } finally {
    loading.value = false
  }
}

onMounted(() => {
  loadCategories()
})
</script>

<style scoped lang="scss">
.products-page {
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
    margin-bottom: 2rem;
  }

  .category-filter {
    display: flex;
    justify-content: center;
    gap: 0.5rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
    padding: 1rem 0;
  }

  .categories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
  }

  .category-link {
    text-decoration: none;
  }

  .product-card, .category-card {
    transition: transform 0.3s, box-shadow 0.3s;

    &:hover {
      transform: translateY(-5px);
      box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
    }

    .product-image {
      width: 100%;
      height: 200px;
      overflow: hidden;
      border-radius: 8px 8px 0 0;
      margin: -16px -16px 16px;

      img {
        width: 100%;
        height: 100%;
        object-fit: cover;
      }
    }

    h3 {
      color: #1e3a8a;
      margin-bottom: 1rem;
    }

    .product-category {
      margin: 1rem 0;
    }

    .product-features {
      margin-top: 1rem;
      padding-left: 1.5rem;

      li {
        margin: 0.5rem 0;
        color: #64748b;
      }
    }
  }

  .empty-state {
    text-align: center;
    padding: 4rem 0;
  }
}
</style>

