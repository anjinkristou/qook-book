Qook Book by Qattous
export .env variables with:
export $(grep -v '^#' .env | xargs)