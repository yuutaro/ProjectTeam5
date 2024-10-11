import React from 'react'

const Index: React.FC = () => {
  return (
    <>
      <div className="w-full h-16 bg-base-100"></div>
      <div className="bg-base-200">
        <h1 className="text-4xl text-center m-24 bg-base-200">データ入力Form</h1>
      </div>
      <div>
        <form className="bg-base-200">
          <div className="m-8">
            <label className="block text-xl">レース名</label>
            <input
              type="text"
              className="w-full p-2 border border-base-300 rounded-md"
              placeholder="レース名を入力してください"
            />
          </div>
          <div className="m-8">
            <label className="block text-xl">レース日</label>
            <input type="date" className="w-full p-2 border border-base-300 rounded-md" />
          </div>
          <div className="m-8">
            <label className="block text-xl">レース場</label>
            <input
              type="text"
              className="w-full p-2 border border-base-300 rounded-md"
              placeholder="レース場を入力してください"
            />
          </div>
          <div className="m-8">
            <label className="block text-xl">レース番号</label>
            <input
              type="number"
              className="w-full p-2 border border-base-300 rounded-md"
              placeholder="レース番号を入力してください"
            />
          </div>
          <div className="m-8">
            <label className="block text-xl">馬番</label>
            <input
              type="number"
              className="w-full p-2 border border-base-300 rounded-md"
              placeholder="馬番を入力してください"
            />
          </div>
          <div className="m-8">
            <label className="block text-xl">馬名</label>
            <input
              type="text"
              className="w-full p-2 border border-base-300 rounded-md"
              placeholder="馬名を入力してください"
            />
          </div>
          <div className="m-8">
            <label className="block text-xl">騎手名</label>
            <input
              type="text"
              className="w-full p-2 border border-base-300 rounded-md"
              placeholder="騎手名を入力してください"
            />
          </div>
          <div className="m-8">
            <label className="block text-xl">枠番</label>
            <input
              type="number"
              className="w-full p-2 border border-base-300 rounded-md"
              placeholder="枠番を入力してください"
            />
          </div>
        </form>
      </div>
    </>
  )
}

export default Index
