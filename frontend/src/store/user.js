import { defineStore } from 'pinia'
import { request } from '@/utils'

export const useUserStore = defineStore('user', {
  state: () => ({
    userInfo: null,
    token: localStorage.getItem('token') || '',
  }),
  getters: {
    isLoggedIn: (state) => !!state.token,
  },
  actions: {
    async login(credentials) {
      try {
        const response = await request.post('/base/access_token', credentials, { noNeedToken: true })
        // Backend returns { code: 200, data: { access_token: ... }, msg: ... }
        if (response.data && response.data.access_token) {
          this.token = response.data.access_token
          localStorage.setItem('token', this.token)
          await this.getUserInfo()
          return response
        }
        throw new Error(response.msg || 'Login failed')
      } catch (error) {
        throw error
      }
    },
    async getUserInfo() {
      try {
        const response = await request.get('/base/userinfo')
        // Backend returns { code: 200, data: {...}, msg: ... }
        this.userInfo = response.data
        return response.data
      } catch (error) {
        this.logout()
        throw error
      }
    },
    logout() {
      this.token = ''
      this.userInfo = null
      localStorage.removeItem('token')
    },
  },
})

