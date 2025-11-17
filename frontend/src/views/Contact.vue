<template>
  <CorporateLayout>
    <div class="contact-page">
      <div class="container">
        <h1>{{ $t('contact.title') }}</h1>
        <p class="description">{{ $t('contact.description') }}</p>

        <div class="contact-content">
          <div class="contact-info">
            <n-card>
              <h2>Get in Touch</h2>
              <div class="info-item">
                <strong>{{ $t('contact.tel') }}:</strong>
                <a href="tel:+886-2608-7707">+886-2608-7707</a>
              </div>
              <div class="info-item">
                <strong>{{ $t('contact.fax') }}:</strong>
                <span>+886-2608-7705</span>
              </div>
              <div class="info-item">
                <strong>{{ $t('contact.email') }}:</strong>
                <a href="mailto:sales@company.com">sales@company.com</a>
              </div>
            </n-card>
          </div>

          <div class="contact-form">
            <n-card>
              <h2>Send us a Message</h2>
              <n-form :model="formData" :rules="rules" ref="formRef">
                <n-form-item path="name" label="Name">
                  <n-input v-model:value="formData.name" placeholder="Your name" />
                </n-form-item>
                <n-form-item path="email" label="Email">
                  <n-input v-model:value="formData.email" placeholder="your.email@example.com" />
                </n-form-item>
                <n-form-item path="message" label="Message">
                  <n-input
                    v-model:value="formData.message"
                    type="textarea"
                    placeholder="Your message"
                    :rows="5"
                  />
                </n-form-item>
                <n-form-item>
                  <n-button type="primary" size="large" @click="handleSubmit">
                    Send Message
                  </n-button>
                </n-form-item>
              </n-form>
            </n-card>
          </div>
        </div>
      </div>
    </div>
  </CorporateLayout>
</template>

<script setup>
import { ref } from 'vue'
import CorporateLayout from '@/layouts/CorporateLayout.vue'
import { NCard, NForm, NFormItem, NInput, NButton, useMessage } from 'naive-ui'

const message = useMessage()
const formRef = ref(null)

const formData = ref({
  name: '',
  email: '',
  message: '',
})

const rules = {
  name: {
    required: true,
    message: 'Please enter your name',
    trigger: 'blur',
  },
  email: {
    required: true,
    type: 'email',
    message: 'Please enter a valid email',
    trigger: 'blur',
  },
  message: {
    required: true,
    message: 'Please enter your message',
    trigger: 'blur',
  },
}

const handleSubmit = async () => {
  try {
    await formRef.value?.validate()
    message.success('Message sent successfully!')
    // Reset form
    formData.value = {
      name: '',
      email: '',
      message: '',
    }
  } catch (error) {
    console.error('Validation error:', error)
  }
}
</script>

<style scoped lang="scss">
.contact-page {
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

  .contact-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 2rem;
  }

  .contact-info,
  .contact-form {
    h2 {
      color: #1e3a8a;
      margin-bottom: 1.5rem;
    }
  }

  .info-item {
    margin: 1rem 0;
    line-height: 1.8;

    strong {
      color: #1e3a8a;
      display: inline-block;
      min-width: 80px;
    }

    a {
      color: #3b82f6;
      text-decoration: none;

      &:hover {
        text-decoration: underline;
      }
    }
  }
}

@media (max-width: 768px) {
  .contact-content {
    grid-template-columns: 1fr;
  }
}
</style>

