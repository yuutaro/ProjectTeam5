import { CartesianGrid, Legend, Line, LineChart, ReferenceDot, Tooltip, XAxis, YAxis } from 'recharts'
import { probability_distribution_data_1 } from './probability_distribution_data'

const TimeChart: React.FC = () => {
  return (
    <>
      <LineChart width={730} height={400} data={probability_distribution_data_1}>
        <CartesianGrid
          verticalCoordinatesGenerator={(props) => {
            return props.width > 450 ? [150, 300, 450] : [200, 400]
          }}
        />
        <Line type="monotone" dataKey="data1" stroke="#8884d8" dot={false} />
        <Line type="monotone" dataKey="data2" stroke="#82ca9d" dot={false} />
        <XAxis dataKey="time" />
        <YAxis />
        <Tooltip />
        <Legend />
      </LineChart>
    </>
  )
}

export default TimeChart
