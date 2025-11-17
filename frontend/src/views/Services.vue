<template>
  <CorporateLayout>
    <div class="services-page">
      <div class="container">
        <h1>{{ $t('services.title') }}</h1>
        <p class="description">{{ $t('services.description') }}</p>

        <!-- Categories Section -->
        <n-spin :show="loadingCategories">
          <div class="categories-section">
            <h2>Our Categories</h2>
            <div class="categories-grid" v-if="categories.length > 0">
              <n-card
                v-for="category in categories"
                :key="category.id"
                class="category-card"
                :class="{ active: selectedCategory?.id === category.id }"
                hoverable
                @click="selectCategory(category)"
              >
                <div class="category-content">
                  <div class="category-icon" v-if="category.icon">
                    <Icon :name="category.icon" />
                  </div>
                  <div class="category-icon" v-else>
                    <IconMdiFolder />
                  </div>
                  <h3>{{ category.name }}</h3>
                  <p v-if="category.description" class="category-description">
                    {{ category.description }}
                  </p>
                </div>
              </n-card>
            </div>
            <div v-else-if="!loadingCategories" class="empty-state">
              <n-empty description="No categories available" />
            </div>
          </div>
        </n-spin>

        <!-- Products Section (shown when category is selected) -->
        <div v-if="selectedCategory" class="products-section">
          <div class="section-header">
            <h2>Products in {{ selectedCategory.name }}</h2>
            <n-button size="small" @click="clearSelection">Show All Categories</n-button>
          </div>
          <n-spin :show="loadingProducts">
            <div class="products-grid" v-if="products.length > 0">
              <n-card v-for="product in products" :key="product.id" class="product-card">
                <template #header v-if="product.image_url">
                  <div class="product-image">
                    <img :src="product.image_url" :alt="product.name" />
                  </div>
                </template>
                <h3>{{ product.name }}</h3>
                <p v-if="product.description">{{ product.description }}</p>
                <ul class="product-features" v-if="product.features && product.features.length > 0">
                  <li v-for="(feature, index) in product.features" :key="index">{{ feature }}</li>
                </ul>
              </n-card>
            </div>
            <div v-else-if="!loadingProducts" class="empty-state">
              <n-empty description="No products in this category">
                <template #icon>
                  <IconMdiPackageVariant />
                </template>
              </n-empty>
            </div>
          </n-spin>
        </div>
      </div>
    </div>
  </CorporateLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import CorporateLayout from '@/layouts/CorporateLayout.vue'
import { NCard, NSpin, NEmpty, NButton } from 'naive-ui'
import api from '@/api'
import Icon from '@/components/Icon.vue'
import IconMdiPackageVariant from '~icons/mdi/package-variant'
import IconMdiFolder from '~icons/mdi/folder'

const categories = ref([])
const products = ref([])
const selectedCategory = ref(null)
const loadingCategories = ref(true)
const loadingProducts = ref(false)

const loadCategories = async () => {
  try {
    loadingCategories.value = true
    const response = await api.getActiveCategories()
    if (response.data) {
      categories.value = response.data
    }
  } catch (error) {
    console.error('Failed to load categories:', error)
  } finally {
    loadingCategories.value = false
  }
}

const loadProducts = async (categoryId) => {
  try {
    loadingProducts.value = true
    const params = { page_size: 100, is_active: true }
    if (categoryId) {
      params.category_id = categoryId
    }
    const response = await api.getProducts(params)
    if (response.data) {
      products.value = response.data
    }
  } catch (error) {
    console.error('Failed to load products:', error)
  } finally {
    loadingProducts.value = false
  }
}

const selectCategory = (category) => {
  selectedCategory.value = category
  loadProducts(category.id)
}

const clearSelection = () => {
  selectedCategory.value = null
  products.value = []
}

onMounted(() => {
  loadCategories()
})
</script>

<style scoped lang="scss">
.services-page {
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

  .categories-section {
    margin-bottom: 3rem;

    h2 {
      font-size: 2rem;
      margin-bottom: 2rem;
      color: #1e3a8a;
      text-align: center;
    }

    .categories-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 1.5rem;
      margin-bottom: 2rem;
    }

    .category-card {
      cursor: pointer;
      transition: all 0.3s ease;
      border: 2px solid transparent;

      &:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
        border-color: #3b82f6;
      }

      &.active {
        border-color: #3b82f6;
        background-color: #eff6ff;
      }

      .category-content {
        text-align: center;
        padding: 0.5rem;

        .category-icon {
          font-size: 3rem;
          color: #3b82f6;
          margin-bottom: 1rem;
          display: flex;
          justify-content: center;
          align-items: center;
        }

        h3 {
          color: #1e3a8a;
          margin: 0.5rem 0;
          font-size: 1.25rem;
        }

        .category-description {
          color: #64748b;
          font-size: 0.9rem;
          margin-top: 0.5rem;
          line-height: 1.5;
        }
      }
    }
  }

  .products-section {
    margin-top: 3rem;
    padding-top: 3rem;
    border-top: 2px solid #e5e7eb;

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 2rem;

      h2 {
        font-size: 2rem;
        color: #1e3a8a;
        margin: 0;
      }
    }

    .products-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 2rem;
    }

    .product-card {
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
        margin-bottom: 0.5rem;
      }

      p {
        color: #64748b;
        margin-bottom: 1rem;
        line-height: 1.6;
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
  }

  .empty-state {
    text-align: center;
    padding: 4rem 0;
  }
}
</style>
