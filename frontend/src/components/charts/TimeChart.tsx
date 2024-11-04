import { CartesianGrid, Legend, Line, LineChart, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'
import { probability_distribution_data_1 } from './probability_distribution_data'

const TimeChart: React.FC = () => {
  return (
    <>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={probability_distribution_data_1}>
          <CartesianGrid strokeDasharray={'3 3'} />
          <Line type="monotone" dataKey="data1" stroke="#8884d8" dot={false} />
          <Line type="monotone" dataKey="data2" stroke="#82ca9d" dot={false} />
          <XAxis dataKey="time" interval={29} />
          <YAxis />
          <Tooltip content={<CustomToolTip active={false} payload={[]} label={''} />} cursor={false} />
          <Legend />
        </LineChart>
      </ResponsiveContainer>
    </>
  )
}

const CustomToolTip: React.FC<{ active: boolean; payload: any[]; label: string }> = ({ active, payload, label }) => {
  if (active && payload && payload.length) {
    // 100分率にして二桁まで表示
    const prob1 = (payload[0].value * 100).toFixed(2)
    const prob2 = (payload[1].value * 100).toFixed(2)
    return (
      <div className="bg-base-100 p-2 rounded-lg shadow-md">
        <p className="prose prose-h6">{`time: ${label} s`}</p>
        <p className="prose prose-p">{`data1: ${prob1} %`}</p>
        <p className="prose prose-p">{`data2: ${prob2} %`}</p>
      </div>
    )
  }
  return null
}

export default TimeChart
