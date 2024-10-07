import { createSlice } from '@reduxjs/toolkit'

// テーマの型定義
type Theme =
  | 'light'
  | 'dark'
  | 'cupcake'
  | 'bumblebee'
  | 'emerald'
  | 'corporate'
  | 'synthwave'
  | 'retro'
  | 'cyberpunk'
  | 'valentine'
  | 'halloween'
  | 'garden'
  | 'forest'
  | 'aqua'
  | 'lofi'
  | 'pastel'
  | 'fantasy'
  | 'wireframe'
  | 'black'
  | 'luxury'
  | 'dracula'
  | 'cmyk'
  | 'autumn'
  | 'business'
  | 'acid'
  | 'lemonade'
  | 'night'
  | 'coffee'
  | 'winter'
  | 'dim'
  | 'nord'
  | 'sunset'

interface ThemeState {
  selectedTheme: Theme
}

const initialState: ThemeState = {
  selectedTheme: 'light', // デフォルトのテーマ
}

const themeSlice = createSlice({
  name: 'theme',
  initialState: initialState,
  reducers: {
    setTheme: (state, action: { type: string; payload: Theme }) => {
      state.selectedTheme = action.payload
    },
  },
})

export const { setTheme } = themeSlice.actions
export default themeSlice.reducer
