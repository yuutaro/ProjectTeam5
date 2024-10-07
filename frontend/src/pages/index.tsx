import { Theme } from 'daisyui'
import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import useSWR from 'swr'
import { setTheme } from '@/redux/slices/themeSlice'
import { RootState } from '@/redux/store'
import { fetcher } from '@/utils'

const Index: React.FC = () => {
  const domain = process.env.NEXT_PUBLIC_BACKEND_URL

  const { data, error } = useSWR(`${domain}`, fetcher)

  const dispatch = useDispatch()
  const currentTheme = useSelector(
    (state: RootState) => state.theme.selectedTheme,
  )

  console.log(currentTheme)

  const toggleTheme = () => {
    const newTheme: Theme = currentTheme === 'light' ? 'dark' : 'light'
    dispatch(setTheme(newTheme))
  }

  if (error) return <div>An error has occurred.</div>
  if (!data) return <div>Loading...</div>

  return (
    <>
      <div>healthcheck: {data.healthcheck}</div>
      <button className="btn btn-secondary" onClick={toggleTheme}>
        Toggle Theme
      </button>
    </>
  )
}

export default Index
