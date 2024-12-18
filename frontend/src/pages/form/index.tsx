import React, { useEffect, useState } from 'react'

const Index: React.FC = () => {
  // 天気
  const weather = ['晴', '曇', '雨', '雪']

  // 競馬場
  const racecourse = ['中山', '東京', '阪神', '京都', '中京', '新潟', '福島', '小倉', '函館', '札幌']

  // 馬場状態
  const ground = ['良', '稍重', '重', '不良']
  type GroundState = '良' | '稍重' | '重' | '不良'
  const [groundState, setGroundState] = useState<GroundState>('良')

  // 出場馬数
  const [totalHorseNum, setTotalHorseNum] = useState<number>(0)

  // 馬番から枠番を計算(馬番, 出場馬の総数)
  const calcFrameNum = (horseNum: number, totalHorseNum: number): number | null => {
    if (horseNum < 1 || horseNum > totalHorseNum) {
      return null // 無効な馬番の場合
    }
    // 基本の頭数と余りを計算
    const baseCount = Math.floor(totalHorseNum / 8) // 各枠に均等に割り当てる馬の数
    const remainder = totalHorseNum % 8 // 余り
    // 枠ごとの馬番範囲を計算
    let start = 1
    for (let frameNum = 1; frameNum <= 8; frameNum++) {
      // 枠に割り当てられる頭数を計算
      const count = baseCount + (frameNum <= remainder ? 1 : 0)
      const end = start + count - 1 // 枠の終了馬番
      // 馬番がこの枠に含まれるかを判定
      if (horseNum >= start && horseNum <= end) {
        return frameNum // 該当する枠番を返す
      }
      start = end + 1 // 次の枠の開始馬番を更新
    }
    return null // ここに到達することは通常ない
  }

  type HorseData = {
    flameNum: number | null // 枠番
    horseNum: number | null // 馬番
    horseName: string // 馬名
    loadWeight: number | null // 斤量(kg)
    jockey: string // 騎手
    trainer: string // 調教師
  }

  const [horseData, setHorseData] = useState<HorseData[]>([])

  // totalHorseNum に応じて horseData を更新する関数
  const updateHorseData = () => {
    const newHorseData: HorseData[] = Array.from({ length: totalHorseNum }, (_, index) => {
      const horseNum = index + 1 // 馬番は1から始まる
      const flameNum = calcFrameNum(horseNum, totalHorseNum)
      return {
        flameNum,
        horseNum,
        horseName: '',
        loadWeight: null,
        jockey: '',
        trainer: '',
      }
    })
    setHorseData(newHorseData)
  }

  // 出場馬数が変更されたら horseData を更新
  useEffect(() => {
    updateHorseData()
    console.log(horseData)
  }, [totalHorseNum])

  return (
    <>
      <div className="h-24 bg-base-100"></div>
      <div className="bg-base-200 md:px-8 md:py-8">
        <div className="m-auto bg-base-100 shadow-md rounded-md">
          <h1 className="prose text-2xl md:text-4xl">入力フォーム</h1>

          {/* レースの基本情報入力フォーム */}
          <div className=" border border-gray-800">
            <h3 className="prose text-2xl">基本情報</h3>
            <div>
              <div>
                <label>日付</label>
                <input type="date" />
              </div>
              <div>
                <label>天候</label>
                <select>
                  {weather.map((w) => (
                    <option key={w}>{w}</option>
                  ))}
                </select>
              </div>
              <div>
                <label>競馬場</label>
                <select>
                  {racecourse.map((r) => (
                    <option key={r}>{r}</option>
                  ))}
                </select>
              </div>
              <div>
                <label>馬場状態</label>
                <select>
                  {ground.map((g) => (
                    <option key={g}>{g}</option>
                  ))}
                </select>
              </div>
              <div>
                <label>出場馬数</label>
                <input type="number" value={totalHorseNum} onChange={(e) => setTotalHorseNum(Number(e.target.value))} />
              </div>
            </div>
          </div>

          {/* 個別の馬の入力フォーム */}
          <div>
            <h3>馬データ</h3>
          </div>
        </div>
      </div>
    </>
  )
}

export default Index

// Code,Rank,Frame Rank,Horse Number,Horse Name,Sex/Age,Kinryou,Jockey,Time,Chakusa,Tsuuka,Nobori,Tansyou,Ninki,Horse Weight,Trainer,Banushi,Shoukin
