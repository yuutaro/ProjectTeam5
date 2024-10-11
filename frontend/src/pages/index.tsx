import Image from 'next/image'
import Link from 'next/link'
import React from 'react'
import { useInView } from 'react-intersection-observer'
import useSWR from 'swr'
import { FadeInBottomWrapper } from '@/components/animation/FadeInBottomWrapper'
import { fetcher } from '@/utils'

const Index: React.FC = () => {
  const domain = process.env.NEXT_PUBLIC_BACKEND_URL

  const { data, error } = useSWR(`${domain}`, fetcher)

  const { ref: heroTitleRef, inView: heroTitleInView } = useInView({
    rootMargin: '-100px', // 100px分だけ上で発火
    triggerOnce: false,
  })

  if (error) return <div>An error has occurred.</div>
  if (!data) return <div>Loading...</div>

  return (
    <>
      {/* キャッチ画像 */}
      <div
        className="min-h-screen bg-no-repeat bg-cover bg-top"
        style={{
          backgroundImage: 'url(/image/horse-race-2714849_1920.jpg)',
        }}
      ></div>

      {/* Hero */}
      <div className="hero bg-base-200 h-auto py-32">
        <div className="hero-content flex-col lg:flex-row">
          {/* <img
            src="https://img.daisyui.com/images/stock/photo-1635805737707-575885ab0820.webp"
            className="max-w-sm rounded-lg shadow-2xl"
          /> */}
          <Image
            src="/image/bremer-rennverein-3283491_1920.jpg"
            alt="Picture of the author"
            width={300}
            height={300}
            className="max-w-sm rounded-lg shadow shadow-black "
          />
          <div>
            <h3
              className={`text-4xl font-bold text-center lg:text-left ${heroTitleInView ? 'animate-fade-left animate-duration-1000' : 'opacity-0'}`}
              ref={heroTitleRef}
            >
              統計データをもとに競馬をしよう
            </h3>
            <FadeInBottomWrapper>
              <p className="p-6">
                本サービスは、膨大な統計データをもとに、精度の高い競馬予想を提供するための画期的なサポートツールです。
                100万件以上の過去レースデータを学習させた高度なAIアルゴリズムにより、これまでのレース結果や騎手・馬のパフォーマンス、
                コースや天候の影響など、複雑な要因を解析し、ユーザーの予想を強力に支援します。
                AIは継続的に学習し、新しいデータやトレンドを取り入れながら、さらに正確な予測を提供。
                初心者からプロの競馬ファンまで、誰でも簡単に利用できる直感的なインターフェースで、
                あなたの馬券戦略を次のレベルへと引き上げます。
              </p>
            </FadeInBottomWrapper>
            <div className="flex justify-center">
              <Link href="/form" className="btn btn-primary mx-auto">
                予測開始!!
              </Link>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default Index
