import React, { useState } from 'react'
import { useDispatch } from 'react-redux'
import { setTheme, Theme, themes } from '@/redux/slices/themeSlice'

export const ThemeSelector: React.FC = () => {
  const dispatch = useDispatch()
  const [selectedTheme, setSelectedTheme] = useState('') // 初期値を空に設定

  const toggleTheme = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const theme = e.target.value as Theme
    setSelectedTheme(theme)
    dispatch(setTheme(theme))
  }

  return (
    <select className="select w-full max-w-xs" value={selectedTheme} onChange={toggleTheme}>
      <option disabled value="">
        Theme
      </option>
      {themes.map((theme) => (
        <option key={theme} value={theme}>
          {theme}
        </option>
      ))}
    </select>
  )
}
