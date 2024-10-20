import { configureStore } from '@reduxjs/toolkit'
import serverHealthReducer from './slices/serverHealthSlice'
import themeReducer from './slices/themeSlice'

export const store = configureStore({
  reducer: {
    theme: themeReducer,
    serverHealth: serverHealthReducer,
  },
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch
