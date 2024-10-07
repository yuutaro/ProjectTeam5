import type { AppProps } from 'next/app'
import '@/styles/globals.css'
import { Provider } from 'react-redux'
import { DrawerWrapper } from '../components/DrawerWrapper'
import { store } from '../redux/store'
import { ThemeProvider } from '@/components/ThemeProvider'

export default function App({ Component, pageProps }: AppProps) {
  console.log('rendering _app.tsx')
  return (
    <Provider store={store}>
      <ThemeProvider>
        <DrawerWrapper>
          <Component {...pageProps} />
        </DrawerWrapper>
      </ThemeProvider>
    </Provider>
  )
}
