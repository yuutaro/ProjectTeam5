import React from 'react'
import useSWR from 'swr'
import { fetcher } from '@/utils'

const Index: React.FC = () => {
  const domain = process.env.NEXT_PUBLIC_BACKEND_URL

  const { data, error } = useSWR(`${domain}`, fetcher)

  if (error) return <div>An error has occurred.</div>
  if (!data) return <div>Loading...</div>

  return (
    <div style={{ backgroundImage: `url("/image/東京競馬場_-_panoramio_(4).jpg")` }}>
      <h1 className="mt-28 text-center text-8xl animate-fade-up animate-once animate-ease-in-out">馬券あたる君</h1>
      <div>health check : {data.healthcheck}</div>
      <div className="p-96"></div>
    </div>
  )
}

export default Index
