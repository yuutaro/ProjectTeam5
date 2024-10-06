import type { AppProps } from 'next/app'
import '@/styles/globals.css'
import { DrawerWrapper } from '@/components/DrawerWrapper'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <>
      <DrawerWrapper Component={Component} pageProps={pageProps} />
      {/* <Component {...pageProps} /> */}
    </>
  )
}
