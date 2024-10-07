import { configureStore } from '@reduxjs/toolkit'
import themeReducer from './slices/themeSlice'

export const store = configureStore({
  reducer: {
    theme: themeReducer, // themeSlice の reducer を登録
  },
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
