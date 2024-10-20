import React from 'react'
import { useDispatch } from 'react-redux'
import { setTheme, Theme, themes } from '@/redux/slices/themeSlice'

export const ThemeSelector: React.FC = () => {
  const dispatch = useDispatch()
  const toggleTheme = (e: React.ChangeEvent<HTMLSelectElement>) => {
    dispatch(setTheme(e.target.value as Theme))
  }

  return (
    <select className="select w-full max-w-xs" onChange={toggleTheme}>
      <option disabled selected>
        Theme
      </option>
      {themes.map((theme) => (
        <option key={theme}>{theme}</option>
      ))}
    </select>
  )
}
