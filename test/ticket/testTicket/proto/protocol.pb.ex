defmodule ForgeAbi.TestTicket do
  @moduledoc false
  use Protobuf, syntax: :proto3

  @type t :: %__MODULE__{
          row: String.t(),
          seat: String.t(),
          room: String.t(),
          time: String.t(),
          name: String.t()
        }
  defstruct [:row, :seat, :room, :time, :name]

  field :row, 1, type: :string
  field :seat, 2, type: :string
  field :room, 3, type: :string
  field :time, 4, type: :string
  field :name, 5, type: :string
end
