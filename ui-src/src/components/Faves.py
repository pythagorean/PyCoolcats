__pragma__('js', '{}', '''
import React from 'react'
import PropTypes from 'prop-types'

const Faves = ({ addFavourite, favourites, hash, removeFavourite }) => {
  return (
    <div>
      {favourites && favourites.includes(hash) ? (
        <button
          onClick={() => removeFavourite(hash)}
          className="glyphicon glyphicon-heart"
          style={{ color: 'red' }}
        />
      ) : (
        <button
          onClick={() => {
            addFavourite(hash)
          }}
          className="glyphicon glyphicon-heart-empty"
          style={{ color: 'red' }}
        />
      )}
    </div>
  )
}

Faves.defaultProps = {
  hash: '',
  favourites: []
}

Faves.propTypes = {
  addFavourite: PropTypes.func.isRequired,
  removeFavourite: PropTypes.func.isRequired
}

export default Faves
''')
