import axios from 'axios'
import { resReject, resResolve, reqReject, reqResolve } from './interceptors'
import { BASE_API } from './helpers'

const axiosInstance = axios.create({
  timeout: 12000,
  baseURL: BASE_API,
})

axiosInstance.interceptors.request.use(reqResolve, reqReject)
axiosInstance.interceptors.response.use(resResolve, resReject)

export const request = axiosInstance

