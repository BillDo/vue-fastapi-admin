import { createI18n } from 'vue-i18n'
import en from './messages/en.json'
import cn from './messages/cn.json'
import vi from './messages/vi.json'

const currentLocale = localStorage.getItem('locale') || 'en'

const i18n = createI18n({
  legacy: false,
  globalInjection: true,
  locale: currentLocale,
  fallbackLocale: 'en',
  messages: {
    en,
    cn,
    vi,
  },
})

export default i18n

