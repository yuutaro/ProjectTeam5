import React from 'react'
import useSWR from 'swr'
import { fetcher } from '@/utils'

const Index: React.FC = () => {
  const domain = process.env.NEXT_PUBLIC_BACKEND_URL

  const { data, error } = useSWR(`${domain}`, fetcher)

  if (error) return <div>An error has occurred.</div>
  if (!data) return <div>Loading...</div>

  return (
    <>
      <div>health check : {data.healthcheck}</div>
      <div className="p-96"></div>
    </>
  )
}

export default Index
