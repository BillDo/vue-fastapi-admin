import { request } from '@/utils'

export default {
  // Public API endpoints for frontend
  login: (data) => request.post('/base/access_token', data, { noNeedToken: true }),
  getUserInfo: () => request.get('/base/userinfo'),
  
  // Products
  getProducts: (params = {}) => request.get('/product/list', { params: { ...params, is_active: true } }),
  getProduct: (id) => request.get('/product/get', { params: { id } }),
  // Categories
  getActiveCategories: () => request.get('/category/active'),
  getCategory: (id) => request.get('/category/get', { params: { id } }),
}

