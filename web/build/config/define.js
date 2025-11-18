import dayjs from 'dayjs'

/**
 * * This defines a global constant, which will be added to the window after startup or packaging.
 * https://vitejs.cn/config/#define
 */

// Project build time
const _BUILD_TIME_ = JSON.stringify(dayjs().format('YYYY-MM-DD HH:mm:ss'))

export const viteDefine = {
  _BUILD_TIME_,
}
