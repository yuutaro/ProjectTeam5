// @ts-ignore
// jstatには型定義はないため、TSを無効化
import { normal } from 'jstat'

// 平均60秒, 標準偏差10秒の正規分布
// 0~120秒の範囲で1秒刻み

export const probability_distribution_data_1 = Array.from({ length: 120 }, (_, i) => {
  const time = i
  const data1 = normal.pdf(time, 60, 10)
  const data2 = normal.pdf(time, 70, 15)
  return { time, data1, data2 }
})
