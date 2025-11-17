<template>
  <CorporateLayout>
    <div class="about-page">
      <div class="container">
        <h1>{{ $t('about.title') }}</h1>
        <p class="description">{{ $t('about.description') }}</p>

        <div class="about-content">
          <n-card>
            <h2>Our Mission</h2>
            <p>
              We are a professional and diversified enterprise specializing in lubricants, 
              precision adhesives, thermal conductive materials, and electronic auxiliary consumables.
            </p>
          </n-card>

          <div class="about-sections">
            <n-card>
              <h3>Who We Are</h3>
              <p>
                A professional and diversified enterprise committed to delivering high-quality 
                products and services to our clients worldwide.
              </p>
            </n-card>

            <n-card>
              <h3>Our Values</h3>
              <p>
                Excellence, innovation, and partnership are at the core of everything we do. 
                We strive to build long-term relationships with our clients based on trust and quality.
              </p>
            </n-card>

            <n-card>
              <h3>Our Commitment</h3>
              <p>
                We are dedicated to providing comprehensive solutions and exceptional service 
                to meet the evolving needs of our customers.
              </p>
            </n-card>
          </div>
        </div>
      </div>
    </div>
  </CorporateLayout>
</template>

<script setup>
import CorporateLayout from '@/layouts/CorporateLayout.vue'
import { NCard } from 'naive-ui'
</script>

<style scoped lang="scss">
.about-page {
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

  .about-content {
    display: flex;
    flex-direction: column;
    gap: 2rem;

    > :first-child {
      h2 {
        color: #1e3a8a;
        margin-bottom: 1rem;
      }

      p {
        font-size: 1.1rem;
        line-height: 1.8;
        color: #64748b;
      }
    }
  }

  .about-sections {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;

    h3 {
      color: #1e3a8a;
      margin-bottom: 1rem;
    }

    p {
      color: #64748b;
      line-height: 1.6;
    }
  }
}
</style>

