import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import axios from 'axios'

interface ServerHealthState {
  loading: boolean
  data: object | null
  status: number | null
  code: string | null
}

const initialState: ServerHealthState = {
  loading: false,
  data: null,
  status: null,
  code: null,
}

export const fetchServerHealth = createAsyncThunk<{ data: object; status: number }, void>(
  'serverHealth/fetchServerHealth',
  async () => {
    try {
      const response = await axios.get('http://localhost:3001/healthcheck')
      // ↑ {"healthcheck":"ok"} が返ってくる
      return { data: response.data, status: response.status, code: null }
    } catch (axiosError: any) {
      if (!axiosError.response) {
        throw axiosError
      }
      return { data: axiosError.data, status: axiosError.response.status, code: axiosError.code }
    }
  },
)

const serverHealthSlice = createSlice({
  name: 'serverHealth',
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(fetchServerHealth.pending, (state) => {
      state.loading = true
    })
    builder.addCase(fetchServerHealth.fulfilled, (state, action) => {
      state.loading = false
      state.data = action.payload.data
      state.status = action.payload.status
    })
    builder.addCase(fetchServerHealth.rejected, (state, action: any) => {
      // typescriptが action.payloadにdataが存在しないというのでanyを書いた(改善要？)
      state.loading = false
      state.data = action.payload?.data
      state.status = action.payload?.status
      state.code = action.payload?.code
    })
  },
})

export default serverHealthSlice.reducer
