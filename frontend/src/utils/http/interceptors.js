// Note: Cannot use useMessage() in interceptors as it requires Vue component context
// Errors are logged to console. Components can show messages using useMessage()

export function reqResolve(config) {
  // Skip token for requests marked with noNeedToken
  if (config.noNeedToken) {
    return config
  }
  
  // Add token to request if available
  const token = localStorage.getItem('token')
  if (token) {
    // Backend expects token in header, not Authorization Bearer
    config.headers.token = token
  }
  return config
}

export function reqReject(error) {
  return Promise.reject(error)
}

export function resResolve(response) {
  const { data } = response
  // Backend returns { code: 200, data: ..., msg: ... }
  if (data.code === 200) {
    return data
  }
  // Handle error response
  console.error('API Error:', data.msg || 'Request failed')
  return Promise.reject(data)
}

export async function resReject(error) {
  let msg = 'Request failed'
  
  if (error.response) {
    const { data, status } = error.response
    
    // Handle 401 unauthorized
    if (status === 401 || data?.code === 401) {
      localStorage.removeItem('token')
      console.error('Session expired. Please login again.')
      // Redirect to login if not already there
      if (window.location.pathname !== '/login') {
        window.location.href = '/login'
      }
      return Promise.reject(error)
    }
    
    msg = data?.msg || error.message || 'Request failed'
  } else if (error.message) {
    if (error.message.includes('timeout')) {
      msg = 'Request timeout'
    } else if (error.message.includes('Network Error')) {
      msg = 'Network error'
    } else {
      msg = error.message
    }
  }
  
  console.error('Request failed:', msg)
  return Promise.reject(error)
}

