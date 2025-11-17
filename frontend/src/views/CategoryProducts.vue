<template>
  <CorporateLayout>
    <div class="products-page">
      <div class="container">
        <h1>{{ categoryName || $t('products.title') }}</h1>

        <div class="back-row">
          <router-link class="back-link" :to="{ name: 'Products' }">{{ $t('common.back') || 'Back to Categories' }}</router-link>
        </div>

        <n-spin :show="loading">
          <div class="products-grid" v-if="products.length > 0">
            <n-card v-for="product in products" :key="product.id" class="product-card">
              <template #header v-if="product.image_url">
                <div class="product-image">
                  <img :src="product.image_url" :alt="product.name" />
                </div>
              </template>
              <template #header v-else>
                <h3>{{ product.name }}</h3>
              </template>
              <h3 v-if="product.image_url">{{ product.name }}</h3>
              <p>{{ product.description }}</p>
              <ul class="product-features" v-if="product.features && product.features.length > 0">
                <li v-for="(feature, index) in product.features" :key="index">{{ feature }}</li>
              </ul>
            </n-card>
          </div>
          <div v-else-if="!loading" class="empty-state">
            <n-empty description="No products available">
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
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'
import CorporateLayout from '@/layouts/CorporateLayout.vue'
import { NCard, NSpin, NEmpty } from 'naive-ui'
import api from '@/api'
import IconMdiPackageVariant from '~icons/mdi/package-variant'

const route = useRoute()
const products = ref([])
const loading = ref(true)
const categoryName = ref('')

const loadCategory = async (id) => {
  try {
    const res = await api.getCategory(id)
    if (res && res.data) categoryName.value = res.data.name
  } catch (e) {
    categoryName.value = ''
  }
}

const loadProducts = async (id) => {
  try {
    loading.value = true
    const res = await api.getProducts({ page_size: 100, category_id: id })
    if (res && res.data && Array.isArray(res.data)) {
      products.value = res.data
    } else {
      products.value = []
    }
  } finally {
    loading.value = false
  }
}

const sync = () => {
  const id = Number(route.params.categoryId)
  if (!Number.isFinite(id)) return
  loadCategory(id)
  loadProducts(id)
}

onMounted(sync)
watch(() => route.params.categoryId, sync)
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
    font-size: 2rem;
    margin-bottom: 1rem;
    color: #1e3a8a;
    text-align: center;
  }

  .back-row {
    text-align: center;
    margin-bottom: 1.5rem;
    .back-link {
      color: #2563eb;
      text-decoration: none;
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
      margin-bottom: 1rem;
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


