import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import axios from 'axios'

interface ServerHealthState {
  data: object | null
  loading: boolean
  error: string | null
}

const initialState: ServerHealthState = {
  data: {},
  loading: false,
  error: null,
}

export const fetchServerHealth = createAsyncThunk('serverHealth/fetchServerHealth', async () => {
  const response = await axios.get('/health')
  // successなら response.data = { healthcheck: 'ok' }
  return response.data
})

const serverHealthSlice = createSlice({
  name: 'serverHealth',
  initialState: initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder.addCase(fetchServerHealth.pending, (state) => {
      state.loading = true
    })
    builder.addCase(fetchServerHealth.fulfilled, (state, action) => {
      state.data = action.payload
      state.loading = false
    })
    builder.addCase(fetchServerHealth.rejected, (state, action) => {
      state.error = action.error.message
      state.loading = false
    })
  },
})

export default serverHealthSlice.reducer
