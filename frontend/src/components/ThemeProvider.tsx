import React from 'react'
import { useSelector } from 'react-redux'
import { RootState } from '@/redux/store'

interface ThemeProviderProps {
  children: React.ReactNode
}

export const ThemeProvider = (props: ThemeProviderProps) => {
  const currentTheme = useSelector(
    (state: RootState) => state.theme.selectedTheme,
  )
  return <div data-theme={currentTheme}>{props.children}</div>
}
