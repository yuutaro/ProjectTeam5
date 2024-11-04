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

type HorseData = {
  // 馬名　ex. メジロマックイーン
  horseName: string
  // 到着時間の確率分布　index: t[s] value: P(t)　ex. [0.1, 0.2, 0.3, 0.4, ...]
  probabilityDistribution: number[]
  // 平均到着時間
  average: number
  // 到着時間の分散
  dispersion: number
}

type ServerResponse = {
  // ここからデータベースのカラム
  // Date,Track,Weather,Race Number,Distance,Condition,Time,Jockey,Trainer,first_horses,second_horses,third_horses
  date: string // 日付 ex. 2021-01-01T12:00:00Z <- GMT-09:00
  track: string // 競馬場 ex. 札幌
  weather: string // 天候 ex. 晴
  raceNumber: number // レース番号 ex. 1
  distance: number // 距離 ex. 1200
  condition: string // 馬場状態 ex. 良
  // 個別の馬のデータ
  horses: HorseData[]
  // オッズなどの加工データ
  
}
const data = [{ horseName: 'メジロマックイーン' }]

const Index: React.FC = () => {
  return (
    <>
      <div className="h-28 w-full bg-base-100"></div>
      <div className="flex flex-col lg:flex-row">
        <TimeChart />
        <div className="h-64 bg-base-200 w-full">
          <h3 className=" font-notosans">確率予測</h3>
        </div>
      </div>
    </>
  )
}

export default Index
