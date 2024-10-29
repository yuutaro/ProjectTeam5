import dynamic from 'next/dynamic'
import React from 'react'

// ssrを無効化するためにはダイナミックインポートを行えばよい。これによりssrを無効化し、クライアントサイドでのみレンダリングされる。
// rechartsのコンポーネントはSSRすると挙動がおかしくなるため、ダイナミックインポートを行う。
// また表示するデータは今後APIから取得するため、いずれにせよクライアントサイドでのみレンダリングする必要がある。
const TimeChart = dynamic(() => import('@/components/charts/TimeChart'), {
  ssr: false,
  loading: () => {
    return (
      <div className="h-[400px] w-[800px] bg-base-100 rounded-xl flex justify-center items-center">
        <span className="loading loading-spinner loading-lg"></span>
      </div>
    )
  },
})

const Index: React.FC = () => {
  return (
    <>
      <div className="h-32 w-full bg-base-100"></div>
      <TimeChart />
    </>
  )
}

export default Index
